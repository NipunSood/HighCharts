from highcharts import Highchart
chart=Highchart()
options={
	'chart':{'type':'scatter'},

	'title':{'text':'Highchart scatter'},
	
	'legend':{'enabled':True},
	
	'xAxis':{'title':'Follow (Thousand)'},

	'yAxis':{'title':{'text':'Friend (Thousand)'}
	}
}

data1=[[161,51],[167,59],[159,49],[157,63],[155,53]]
data2=[[179,165],[175,171],[193,180],[186,172],[187,178]]

chart.set_dict_options(options)

chart.add_data_set(data1,'scatter','Celebrity Accounts',color='rbga(223,83,8,5)')
chart.add_data_set(data2,'line','Normal User Accounts',color='rbga(119,152,19,8)')

chart.save_file('/scatter-highCharts')