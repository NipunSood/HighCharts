from highcharts import Highchart
import datetime
chart=Highchart()
options={
	'chart':{'type':'bubble'},

	'title':{'text':'Highchart bubble'},
	
	'legend':{'enabled':True},

	'xAxis':{'type':'datetime',
	'dateTimeLabelFormats':{
	#%e represent day of the month %b represent short months like jan,feb,dec so on.
		'day':'%e %b',
	#%b represent short of each of the month and %y two last digit of year like if year is 2016 it will print 16	
		'month':'%b, %y',
	#%Y represent all the four digits of the year.	
		'year':'%Y' },
	}
}
#In datetime.datetime(year,month,date),User_NO.,Total number of tweets.
data1=[[datetime.datetime(2016,5,9),1,28],[datetime.datetime(2016,5,10),1,44],[datetime.datetime(2016,5,21),1,21],[datetime.datetime(2016,5,12),1,19],[datetime.datetime(2016,5,13),1,27],[datetime.datetime(2016,5,17),1,35],[datetime.datetime(2016,5,18),1,22],[datetime.datetime(2016,5,19),1,36],[datetime.datetime(2016,5,20),1,31],[datetime.datetime(2016,5,23),1,36],[datetime.datetime(2016,5,24),1,49],[datetime.datetime(2016,5,25),1,49],[datetime.datetime(2016,5,26),1,29],[datetime.datetime(2016,5,27),1,36],[datetime.datetime(2016,5,30),1,4],[datetime.datetime(2016,5,31),1,2],[datetime.datetime(2016,6,1),1,4],[datetime.datetime(2016,6,3),1,3],[datetime.datetime(2016,6,6),1,5]]

data2=[[datetime.datetime(2016,5,13),1,5],[datetime.datetime(2016,6,6),1,6],[datetime.datetime(2016,6,7),1,16],[datetime.datetime(2016,6,8),1,2],[datetime.datetime(2016,6,10),1,12]]

data3=[[datetime.datetime(2016,5,9),1,63],[datetime.datetime(2016,5,10),1,77],[datetime.datetime(2016,5,11),1,15],[datetime.datetime(2016,5,16),1,66],[datetime.datetime(2016,5,17),1,120],[datetime.datetime(2016,5,18),1,15],[datetime.datetime(2016,5,19),1,79],[datetime.datetime(2016,5,20),1,63],[datetime.datetime(2016,5,23),1,70],[datetime.datetime(2016,5,24),1,98],[datetime.datetime(2016,5,25),1,181],[datetime.datetime(2016,5,26),1,67],[datetime.datetime(2016,5,27),1,168],[datetime.datetime(2016,5,31),1,9],[datetime.datetime(2016,6,1),1,32],[datetime.datetime(2016,6,2),1,8],[datetime.datetime(2016,6,3),1,54],[datetime.datetime(2016,6,6),1,28],[datetime.datetime(2016,6,7),1,32],[datetime.datetime(2016,6,8),1,19]]

data4=[[datetime.datetime(2016,5,9),1,30],[datetime.datetime(2016,5,10),1,16],[datetime.datetime(2016,5,11),1,15],[datetime.datetime(2016,5,12),1,15],[datetime.datetime(2016,5,13),1,30],[datetime.datetime(2016,5,25),1,5],[datetime.datetime(2016,5,26),1,1],[datetime.datetime(2016,6,2),1,9],[datetime.datetime(2016,6,3),1,6],[datetime.datetime(2016,6,6),1,19],[datetime.datetime(2016,6,7),1,3],[datetime.datetime(2016,6,8),1,4]]

chart.set_dict_options(options)

chart.add_data_set(data1,'bubble','user1')
chart.add_data_set(data2,'bubble','user2')
chart.add_data_set(data3,'bubble','user3')
chart.add_data_set(data4,'bubble','user4')


chart.save_file('/bubble-highCharts')