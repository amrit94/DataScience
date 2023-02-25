## 20 Feb Assignment Solution 
### Q1. What is Web Scraping? Why is it Used? Give three areas where Web Scraping is used to get data.

Web scraping is an automatic method to obtain large amounts of data from websites.
Most of this data is unstructured data in an HTML format which is then converted into structured data
in a spreadsheet or a database so that it can be used in various applications

Used for
* Price Monitoring
* Market Research
* News Monitoring
* Sentiment Analysis
* Email Marketing

**Shopping Sites:**
Some several websites and applications can help you to easily compare pricing between several retailers for the same product.

**Real Estate Listing:**
Many real estate agents use web scraping to populate their database of available properties for sale or for rent.

**Industry Statistics and Insights:**
Many companies use web scraping to build massive databases and draw industry-specific insights from these.
These companies can then sell access to these insights to companies in said industries.

**Lead Generation**
One incredibly popular use of web scraping is lead generation. 
This use is so popular in fact, that we have written an entire guide on using web scraping for lead generation.



### Q2. What are the different methods used for Web Scraping?
**HTML Parsing**
HTML parsing involves the use of JavaScript to target a linear or nested HTML page.
It is a powerful and fast method for extracting text and links (e.g. a nested link or email address), scraping screens and pulling resources.

**DOM Parsing**
The Document Object Model (DOM) defines the structure, style and content of an XML file.
Scrapers typically use a DOM parser to view the structure of web pages in depth

**XPath**
XPath is short for XML Path Language, which is a query language for XML documents.
XML documents have tree-like structures, so scrapers can use XPath



### Q3. What is Beautiful Soup? Why is it used?
Beautiful Soup provides simple methods for navigating, searching, and modifying a parse tree in HTML, XML files.

* It transforms a complex HTML document into a tree of Python objects.
* It also automatically converts the document to Unicode, so you don’t have to think about encodings
* This tool not only helps you scrape but also to clean the data


### Q4. Why is flask used in this Web Scraping project?
* Flask is a lightweight framework to build websites.
* These can be used to scrap data and display all data on the go.


### Q5. Write the names of AWS services used in this project. Also, explain the use of each service.
**AWS Elastic Beanstalk** is an orchestration service offered by Amazon Web Services for deploying applications which orchestrates various AWS services, including EC2, S3, Simple Notification Service, CloudWatch, autoscaling, and Elastic Load

**AWS CodePipeline** is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates.