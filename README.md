# restaurant-example

this project is exam code in coursera meta course.

description of exam:

Introduction

This reading is an overview of the scope of the project, all the necessary endpoints, and notes that you will have to implement in the final project. This reading will help you to successfully complete the project so read it carefully and reference it while developing your API project to help you keep on track.
Scope

You will create a fully functioning API project for the Little Lemon restaurant so that the client application developers can use the APIs to develop web and mobile applications. People with different roles will be able to browse, add and edit menu items, place orders, browse orders, assign delivery crew to orders and finally deliver the orders. 

The next section will walk you through the required endpoints with an authorization level and other helpful notes. Your task is to create these endpoints by following the instructions. 
Structure 

You will create one single Django app called LittleLemonAPI and implement all API endpoints in it. Use pipenv to manage the dependencies in the virtual environment. Review the video about Creating a Django Project using pipenv.
Function or class-based views

You can use function- or class-based views or both in this project. Follow the proper API naming convention throughout the project. Review the video about Function- and class-based views as well as the video about Naming conventions.
User groups

Create the following two user groups and then create some random users and assign them to these groups from the Django admin panel. 

     Manager

    Delivery crew
    
 API endpoints 

Here are all the required API routes for this project grouped into several categories.
User registration and token generation endpoints 

You can use Djoser in your project to automatically create the following endpoints and functionalities for you.

![image](https://user-images.githubusercontent.com/39513943/234649841-809faf94-f8ab-47d9-b90f-cff0021729cc.png)

 Menu-items endpoints
 
 ![image](https://user-images.githubusercontent.com/39513943/234650030-e1af83d2-4bed-498c-ad47-839894b59f1b.png)
 ![image](https://user-images.githubusercontent.com/39513943/234650161-cbc3eae6-01f0-42c2-80b2-4d35e6aef595.png)
 
 User group management endpoints
 
 ![image](https://user-images.githubusercontent.com/39513943/234650371-9fe2cb62-d535-438a-8d71-ba6b6cfedff4.png)
 
 ![image](https://user-images.githubusercontent.com/39513943/234650472-65765e47-0755-40c7-bdf9-435d58a9b905.png)
 
 Order management endpoints
 
 ![image](https://user-images.githubusercontent.com/39513943/234650662-04a7fbfe-2c95-4038-89dd-12c2e6af156a.png)
 ![image](https://user-images.githubusercontent.com/39513943/234650772-8a5ba50d-a10a-4c7d-9062-9ee5a7019207.png)






