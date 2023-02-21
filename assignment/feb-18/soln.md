## 18 Feb Assignment Solution 

### Q1. What is an API? Give an example, where an API is used in real life.
API stands for `Application Programming Interface`.
Its a software interface that allows `two applications to interact` with each other without any user intervention.

Popular API Examples:
* **Google Maps API’s**: Google Maps APIs allows developers to use Google Maps on Webpages.
* **YouTube API’s**: Google’s API lets developers integrate YouTube and functionality into websites or applications.

Usage
* API helps `two different software’s to communicate` and exchange data with each other.
* Simple, flexible, quickly adopted.


### Q2. Give advantages and disadvantages of using API. 
* Advantages
  * Increased Visibility and Traffic
  * Seamless Integration
  * Increased Efficiency
  * Easier Maintenance
* Disadvantages
  * Increased Complexity
  * Limited Functionality
  * Dependency on Third Party Services
  * Security and Privacy Risks


### Q3. What is a Web API? Differentiate between API and Web API.
Web API is an API as the name suggests, it can be accessed over the web using the `HTTP protocol`. It a subset of API.

A Web API or Web Service API is an application processing interface `between a web server and web browser`. All web services are APIs but not all APIs are web services. REST API is a special type of Web API that uses the standard architectural style.

TCP, SMTP, HTTP protocals are use in API but in Web API only HTTP protol is used.

### Q4. Explain REST and SOAP Architecture. Mention shortcomings of SOAP.
* **SOAP APIs**
  * These APIs use Simple Object Access Protocol. Client and server exchange messages using XML.
  * This is a less flexible API that was more popular in the past.
* **REST APIs**
  * These are the most popular and flexible APIs found on the web today.
  * The client sends requests to the server as data.
  * The server uses this client input to start internal functions and returns output data back to the client.
* Mention shortcomings of SOAP
  * Poorer performance, more complexity, less flexibility.
  * API calls cannot be cached.
  * Message format	- Only XML.

### Q5. Differentiate between REST and SOAP.
* SOAP API
    * Simple Object Access Protocol
    * Protocol Used: TCP or SMTP
    * Data Transfer: XML (WSDL)
    * More secure than REST API
    * Preffered Choise: Offline application 
* REST API
    * Representational State Transfer 
    * Protocol Used: HTTP
    * Data Transfer: JSON
    * Less secure than SOAP API
    * Preffered Choise: Web based application
    * Fxn: PUT, GET
    * Simple, Scalable and flexible