# Pharmacy-Management-System : Project Overview :

Welcome to the Pharmacy Management System! This project is designed as an introduction to databases, MySQL, and Python with Tkinter GUI. This application allows you to efficiently manage your pharmacy's medicine inventory. You can easily add new medicines, update existing ones, and keep track of all your medicines. The system is divided into three main sections:

## Sections of the App

### 1. New Medicine Add Department

In this section, you can :

  * **Add New Medicines :** Input the reference number and name of any new medicine to add it to the database.
  * **Modify Existing Medicines :** Update the name of any existing medicine.
  * **Delete Medicines :** Remove any medicines that are no longer required.
All newly added medicines are stored and displayed in a table in this section. Operation buttons for adding, modifying, and deleting are conveniently located next to this medicine table.

### 2. Medicine Information

This section allows you to :

  * **Add Information :** Update and add information regarding newly added medicines.
  * **Modify Existing Records :** Update information for existing medicines.
  * **Delete Records :** Remove any medicine records as needed.

All operation buttons for these actions are located just below this section. All the medicines along with their information are stored and displayed in the inventory table present below this sectio.

### 3. Final Database Inventory

This section displays all the medicines present in your inventory along with their corresponding information. You can :

  * **Select Medicines :** Choose any medicine from the inventory.
  * **Perform Operations :** Use the "Medicine Information" section and operation buttons (located just above this section) to add, update, or delete medicine information.

### 4. Search By Option

This feature helps you search for a medicine in your final inventory using :
  * Reference number
  * Lot number
  * Medicine name

## Steps to run the application

Software Requirement :

1. IDE - VSCode or Pycharm
2. Xampp for MYSQL

Frontend Language : Python

Backend Database : MySQL

Packages :

1. Install the required packages by running the following command :
   ```bash
   pip install -r requirements.txt
   ```
2. Install tkinter 
3. Install all the required packages used in the import section

Steps :

1. Download MySQL Community Server
2. Download XAMPP : Start the Apache and MySQL servers.
3. Open Xampp and click on "Go to Application" then click on "phpMyAdmin".
4. Now create a new database named "management". Then go to the "Import" tab and import the "management.sql" file.
5. You can also create a new user with a new password in the "User Accounts" tab.
6. Update MySQL User and Password : If you have set a password for your MySQL user account or use a username other than 'root', update the user and password in the code wherever the conn connection (conn=mysql.connector.connect(host="localhost",user="root",password="",database="management")) is established.
By default, the user is root with no password set.
7. Run the code! Enjoy!

## Screenshot 

<img width="1440" alt="Screenshot 2024-07-17 at 4 51 00 PM" src="https://github.com/user-attachments/assets/775198bf-9b60-4ba2-9aaf-6b95599b9c2e">

