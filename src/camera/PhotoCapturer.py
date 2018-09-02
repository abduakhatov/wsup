from time import sleep
from picamera import PiCamera


def take_photo():
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    sleep(2)
    pic_name = "{timestamp:%d%m%Y}/img-{timestamp:%d%m%Y %H:%M:%S}-{counter:03d}"
    try:
        camera.capture('../img/{}.jpg'.format(pic_name))
    except Exception as exception:
        print(exception, "\n")
        raise exception
        return exception
    finally:
        camera.close()



    return pic_name


