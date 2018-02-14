def _convert_to_degress(value):
    d = float(value[0][0]) / float(value[0][1])
    m = float(value[1][0]) / float(value[1][1])
    s = float(value[2][0]) / float(value[2][1])
    return d + (m / 60.0) + (s / 3600.0)


def get_exif_location(gpsexif):
    lat = None
    lon = None

    gps_latitude = gpsexif['GPSLatitude']
    gps_latitude_ref = gpsexif['GPSLatitudeRef']
    gps_longitude = gpsexif['GPSLongitude']
    gps_longitude_ref = gpsexif['GPSLongitudeRef']

    if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
        lat = _convert_to_degress(gps_latitude)
        if gps_latitude_ref != 'N':
            lat = 0 - lat

        lon = _convert_to_degress(gps_longitude)
        if gps_longitude_ref != 'E':
            lon = 0 - lon

    return lat, lon
