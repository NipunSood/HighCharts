from highcharts import Highchart
chart=Highchart()
options={
	'chart':{'type':'line'},

	'title':{'text':'Highchart line'},
	
	'legend':{'enabled':True},
	
	'xAxis':{'categories':['Jan','Feb','Mar','Apr','Sep','Oct','Nov','Dec'],
	'title':'Months of the year'},

	'yAxis':{'title':{'text':'Number of followers'}
	}
}

data1=[7,7,9,14,18,21,25,26,30,55,62,88]
data2=[11,17,22,25,56,76,91,182,150]
data3=[3,4,5,8,11,15,17,36,42,106,126,148]
chart.set_dict_options(options)

chart.add_data_set(data1,'line','user1')
chart.add_data_set(data2,'line','user2')
chart.add_data_set(data3,'line','user3')


chart.save_file('/line-highCharts')