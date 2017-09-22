import os,time
print" #####################"
print"          ##                        ##                       ###"
print"          ##                       ## ##                 ###     ###"
print"          ##                      ##   ##               ##         ##"
print"          ##                     ##     ##             ##           ##"
print"          ##                    ##       ##           ##             ##"
print"          ##                   ## ### ### ##         ##               ##"
print"          ##                  ##           ##         ##             ##"
print"          ##                 ##             ##         ##           ##"
print"          ##                ##               ##         ###        ###"
print"          ##              ##                  ##             ###"
pos_x=10
pos_y=80
vel_x=60
vel_y=2
pos_x += vel_x
pos_y += vel_y
if pos_x > 100 or pos_x 0:
   vel_x = -vel_x
if pos_y > 100 or pos_y 0:
   vel_y = -vel_y
time.sleep(5)
