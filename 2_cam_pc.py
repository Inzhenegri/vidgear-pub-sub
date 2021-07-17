from vidgear.gears import NetGear
import cv2
import threading


# def camera_1():
#     while True:
        # frame_1 = client_1.recv()
        # if frame_1 is None:
        #     break
        # print('camera_1 is work')
        # cv2.imshow('frame_1', frame_1)

        # key = cv2.waitKey(1)
        # if key == ord('q'):
        #     cv2.destroyAllWindows()
        #     break


# def camera_2():
#     while True:
    #     frame_2 = client_2.recv()
    #     if frame_2 is None:
    #         break
    #     print('camera_2 is work')
    #     cv2.imshow('frame_2', frame_2)

    #     key = cv2.waitKey(1)
    #     if key == ord('q'):
    #         cv2.destroyAllWindows()
    #         break

options = {
    'flag': 0,
    'copy': False,
    'track': False
}

client_1 = NetGear(
    address='192.168.11.159', # school network
    # address='192.168.11.137', # home network
    port='5462',
    pattern=2,
    receive_mode=True,
    logging=True,
    protocol='tcp',
    **options
)

client_2 = NetGear(
    address='192.168.11.159', # school network
    # address='192.168.11.137', # home network
    port='5463',
    pattern=2,
    receive_mode=True,
    logging=True,
    protocol='tcp',
    **options
)

def start():
    while True:
        frame_1 = client_1.recv()
        frame_2 = client_2.recv()

        if frame_1 is None:
            break
        if frame_2 is None:
            break

        cv2.imshow('frame_1', frame_1)
        cv2.imshow('frame_2', frame_2)

        key = cv2.waitKey(1)
        if key == ord('q'):
            cv2.destroyAllWindows()
            break

start_thread = threading.Thread(target=start, args=())
start_thread.start()

# camera_thread_1 = threading.Thread(target=camera_1, args=([frame_1, ]))
# camera_thread_2 = threading.Thread(target=camera_2, args=([frame_2, ]))

# camera_thread_1.start()
# camera_thread_2.start()

while True:
    pass

# cv2.destroyAllWindows()
# client_1.close()
# client_2.close()
