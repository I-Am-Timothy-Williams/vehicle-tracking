# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:01:08 2023

@author: Timot
"""
from scipy.optimize import linear_sum_assignment as linear_assignment_
import deepsort
from deepsort import deepsort_rbc
from deepsort import get_get

import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
            
        #Initialize deep sort.
        deepsort = deepsort_rbc(wt_path='ckpts/model640.pt')
### START DEEPSORT
            
            print(frame_id)

            detections,out_scores = get_gt(frame,frame_id,gt_dict)

            if detections is None:
                print("No dets")
                frame_id+=1
                continue

            detections = np.array(detections)
            out_scores = np.array(out_scores) 

            tracker,detections_class = deepsort.run_deep_sort(frame,out_scores,detections)

            for track in tracker.tracks:
                if not track.is_confirmed() or track.time_since_update > 1:
                    continue
			
            bbox = track.to_tlbr() #Get the corrected/predicted bounding box
            id_num = str(track.track_id) #Get the ID for the particular track.
            features = track.features #Get the feature vector corresponding to the detection.

			#Draw bbox from tracker.
            cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])),(255,255,255), 2)
            cv2.putText(frame, str(id_num),(int(bbox[0]), int(bbox[1])),0, 5e-3 * 200, (0,255,0),2)
            
            out.write(frame)














    # # shortlist contours appearing in the detection zone
    # vehicles_down = 0
    # for cntr in bounding_rect:
    #     x,y,w,h = cv2.boundingRect(cntr)
    #     if (x <= 200) & (y >= 80) & (cv2.contourArea(cntr) >= 25):
    #         if (y >= 90) & (cv2.contourArea(cntr) < 40):
    #             break
    #    
        ##
                # gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
                # contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
                # # print(len(contours))
                # for cntr in contours:
                #     x,y,w,h = cv2.boundingRect(cntr)
                #     #print(cv2.contourArea(cntr))
                #     if (x <= 640) & (y >= 320) & (cv2.contourArea(cntr) >= 7000):
                #         # print('bye')
                #         vehicles_down = vehicles_down + 1
                #         if (y >= 350) & (cv2.contourArea(cntr) < 10000):
                #             # print('hello')
                #             break
                # for cntr in bounding_rect:
                #     x,y,w,h = cv2.boundingRect(cntr)
                #     if (x <= 640) & ( y >= 320):
                #         #print('hello world')
                #         if (y >= 1000):
                #            # print("hello world")
                #             break
                        # vehicles_down = vehicles_down + 1

        ##   
        # if (x1 <= 640) & (y1 >= 320) & (y1 <= 340):
        #     vehicles_down = vehicles_down + 1
        # if(y1 >= 340):                            
        #     print('hello')
#"""     # Put outside this for loop, try contour again """
        # print(vehicles_down)        
        # cv2.putText(frame, "Vehicles down: " + str(vehicles_down), (55, 15), font, 0.6, (0, 180, 0), 2)
!pip install -r requirements.txt
