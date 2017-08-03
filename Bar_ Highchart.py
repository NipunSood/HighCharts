from highcharts import Highchart
chart=Highchart()
options={
	'chart':{'type':'bar'},

	'title':{'text':'Highchart bar'},
	
	'legend':{'enabled':True},
	
	'xAxis':{'categories':['User 1','User 2','User 3','User 4','User 5']},

	'yAxis':{'title':{'text':'Number of followers (thousands)'}
	}
}

data1=[107,31,635,2032]
data2=[133,156,947,988,6]
data3=[973,314,4054,732,34]
data4=[1052,954,4250,740,38]

chart.set_dict_options(options)

chart.add_data_set(data1,'bar','day1')
chart.add_data_set(data2,'bar','day2')
chart.add_data_set(data3,'bar','day3')
chart.add_data_set(data4,'bar','day4')

chart.save_file('/bar-highCharts')