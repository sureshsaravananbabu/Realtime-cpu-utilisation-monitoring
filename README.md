# Realtime-cpu-utilisation-monitoring
#First module will  generate the gauge chart for CPU and RAM utilisation.

#Second module will generate the  for CPU and RAM utilisation in single line chart.

#Third module will send the email when there is ram utilisation is over 50% for 10 seconds.

1)This project is developed with help of django channels package.It will create the channel to continously send the stream of real time data for every second from backend  to the front end.

2)In the front end using socket,Establish the connection to the channel and get the data sent in the backend and  display the data in different styles of format

3)Get Emailid during the loading of page using javascript and send it to backend for processing .if the RAM utilisation is continously greater than 50% an Email will  be  sent to user with help of django.core.mail.backends.smtp.EmailBackend

