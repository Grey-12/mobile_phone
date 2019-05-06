## Gsmarena Xpath

- sample url: www.gsmarena.com/makers.php3
'''
	//td/a/@href  # get all brand
'''

- sample url: www.gsmarena.com/acer-phones-59.php
'''
	//div[@class='makers']//a/@href  # get all model url
	//a[@class='pages-next']/@href  # get the next page url
'''

- sample url: www.gsmarena.com/samsung_galaxy_tab_8_9_p7310-3893.php
'''
	//meta[@name='Description']/@content   # get the website SEO word
	//h1  # get brand and model
	//td[@data-spec='os']/text()  # get the model's os
	//p[@data-spec='comment']/text()  # maybe have comment,i need get it
'''
