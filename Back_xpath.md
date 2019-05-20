## Gsmarena Xpath

- sample url: www.gsmarena.com/makers.php3

```Xpath
//td/a/@href  # get all brand
```

- sample url: www.gsmarena.com/acer-phones-59.php

```Xpath
//div[@class='makers']//a/@href  # get all model url
//a[@class='pages-next']/@href  # get the next page url
```

- sample url: www.gsmarena.com/samsung_galaxy_tab_8_9_p7310-3893.php

```Xpath    
//meta[@name='Description']/@content   # get the website SEO word
//h1  # get brand and model
//td[@data-spec='os']/text()  # get the model's os
//p[@data-spec='comment']/text()  # maybe have comment,i need get it
```

## China-price Xpath

- sample url: http://www.china-prices.com/tvbox/1

```xpath
//div[@class='product']/div[@class='product-title']/a/@href  # get SKU's url
the page is url's last number
```

- sample url: http://www.china-prices.com/tvbox/15609/alfawise-a9x

```xpath
//div[@class='row']/div[contains(text(), "Brand")]//../following-sibling::div[1]/text()  # get brand
//div[@class='row']/div[contains(text(), "Model")]//../following-sibling::div[1]/text()  # get model
//div[@class='row']/div[contains(text(), "Type")]//../following-sibling::div[1]/text()  # get type(maybe the type is null)
```


