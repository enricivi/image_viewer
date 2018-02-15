from PyQt5.QtCore import QModelIndex, Qt, QAbstractListModel
from PyQt5.QtGui import QPixmap, QIcon
from PIL import Image, ExifTags
from PIL.ImageQt import ImageQt

class ImageListModel(QAbstractListModel):
    def __init__(self, paths=list(), parent=None):
        super(ImageListModel, self).__init__(parent)
        self.images = list()
        self.insertRows(paths)

    def insertRows(self, paths=list(), parent=QModelIndex()):
        im = self.read_images(paths)
        self.beginInsertRows(parent, len(self.images), len(im))
        self.images += im
        self.endInsertRows()
        return True

    def removeRows(self, row: int, count: int, parent=QModelIndex()):
        self.beginRemoveRows(parent, row, row+count-1)
        for idx in range(count-1, -1, -1):
            self.images.pop(row+idx)
        self.endRemoveRows()
        return True

    def data(self, index: QModelIndex, role: int = ...):
        image = self.images[index.row()]
        if (role == Qt.DisplayRole):
            return image.get_filename()
        elif (role == Qt.DecorationRole):
            return QIcon( QPixmap.fromImage(image.get_thumbnail()) )

    def rowCount(self, parent: QModelIndex = ...):
        return len(self.images)

    def read_images(self, paths):
        ims = list()
        for path in paths:
            try:
                ims.append(SingleImage(path))
            except Exception as e:
                print("Exception: {}".format(e))
        return ims

    def get_image(self, row):
        return self.images[row].get_ImageQT()

    def get_exif(self, row):
        im = self.images[row]
        exif = im.get_exif().items() if (im.get_exif() is not None) else dict().items()
        exif = {ExifTags.TAGS[e]: v for e, v in exif if e in ExifTags.TAGS}
        if ('GPSInfo' in exif):
            gps = dict()
            for key in exif['GPSInfo'].keys():
                gpsdecoded = ExifTags.GPSTAGS.get(key, key)
                gps[gpsdecoded] = exif['GPSInfo'][key]
            exif['GPSInfo'] = gps
        return exif


class SingleImage():
    def __init__(self, path: str, thumb_size=(75, 75)):
        self.path = path
        self.image = Image.open(path)

        self.thumbnail = self.image.copy()
        self.thumbnail.thumbnail(size=thumb_size)

    def get_ImageQT(self):
        return ImageQt(self.image)

    def get_thumbnail(self):
        return ImageQt(self.thumbnail)

    def get_filename(self):
        return self.path.split('/')[-1]

    def get_exif(self):
        return self.image._getexif()
