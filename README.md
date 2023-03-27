# staff_records_web_app
<h3>This web app allows the user to query/update staff records SQL database</h3>
<h6>Designed & Written by David Manuel Vidal</h6>

(ALL STAFF NAMES IN THE DATABASE ARE FOR DEMO PURPOSES ONLY. THEY DO NOT REPRESENT REAL PEOPLE.)

<h3>To Run:</h3>
- Download this repository
- Navigate to staff_recods_web_app/ directory
- type flask run in terminal (if you do not already have flask, run pip install flask and pip install Flask-Mail)
- copy/paste URL into browser

<h3>To Test App:</h3>
  - Register in /register, then login and explore!
  
  
<h1>Routes:</h1>

<h4>REGISTER:</h4>
<h6>/register</h6>
   - Simply create a username and password to register
   - Select a security question. This will be used if you ever forget your password or need to reset your password.

LOGIN:
/login
   - Once you have registered, you will be redirected to the login page.
   - If you forget your password, you can always reset it using you security question. Click 'Forgot Password/Reset Password' from the login page to do this.
 
DEPARTMENTS:
/departments
  - This route lets you choose any department (or all departments) and sort the staff names by various criteria.
       - The desired data is retrieved from a SQL database and displayed on screen.
  - You may click the up/down arrows by any column to re-sort.
  - You may type your email in the text field to have a CSV of the chosen department (sorted by the criteria of your choosing) sent to your e-mail.
  - You may also click the Download CSV button to be redirected to download the CSV

ALL DEPARTMENTS
/all_departments
  - This route redirects you to /departments, automatically populating the all departments option.
 
Add NEW STAFF:
/add_new_staff
  - Enter the required information of a staff member.
  - The staff member will be added to the appropriate SQL databases and you will see their information populate in the any of the apporpriate routes.

REMOVE STAFF:
/remove_staff
   - A manager PIN is typically required to remove a staff member. However, for this demo, you may use '0000' to test this feature out!
   - Once a staff member is removed, their information is added to a former_staff database, which you can access from the /former_staff route
   

STAFF_LOOKUP:
/staff_lookup
   - This route allows you type in partial information to find any staff member.
        - (i.e. if 'ar' is typed in the text field and 'First Name' is selected from the dropdown menu, all staff members with 'ar' anywhere in their first name will be displayed).
   - All staff members who match the search criteria will populate
   
EDIT STAFF:
/edit_staff
   - This route allows you to edit any of the staff information
     - First search for the staff member you wish to edit, using a similar method to staff_lookup (typing partial information will display all matchin results)
     - Next, select the staff member you wish to edit.
     - Last, select the item you wish to edit and type in the new value you wish to assign to that item.
   
SALARY:
/salary
    - This route simply displays a table of all staff members and their corresponding salaries.
  
