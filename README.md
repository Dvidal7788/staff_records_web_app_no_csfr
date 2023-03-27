# staff_records_web_app
<h6>Designed & Written by David Manuel Vidal</h6>
<h6>(All staff names in the database are for demo purposes only. They do not represent real people.)</h6>
<h3>Purpose:</h3>
<h4>This web app allows the user to query/update staff records SQL database</h4>

<h3>To Run:</h3>
<ul>
  <li>Download this repository</li>
  <li>Navigate to staff_recods_web_app/ directory</li>
  <li>type flask run in terminal (if you do not already have flask, run pip install flask and pip install Flask-Mail)</li>
  <li>copy/paste URL into browser</li>
</ul>

<h3>To Test App:</h3>
<ul>
  <li>Click the 'Register' link in the top right corner</li>
  <li>Register, then log in</li>
</ul>
![Register Screenshot](https://drive.google.com/file/d/18q-YDsYbYcoI5EYGKDxnELyV084ylRxi/view?usp=sharing)
  
  
<h1>Routes:</h1>

<h5>REGISTER:</h5>
<h6>/register</h6>
<ul>
   <li>Simply create a username and password to register</li>
   <li>Select a security question. This will be used if you ever forget your password or need to reset your password.</li>
</ul>

<h5>LOGIN:</h5>
<h6>/login</h6>
<ul>
   <li>Once you have registered, you will be redirected to the login page.</li>
   <li>If you forget your password, you can always reset it using you security question. Click 'Forgot Password/Reset Password' from the login page to do this.</li>
</ul>

<h5>DEPARTMENTS:</h5>
<h6>/departments</h6>
<ul>
  <h6>
  <li>This route lets you choose any department (or all departments) and sort the staff names by various criteria.</li>
  <li>The desired data is retrieved from a SQL database and displayed on screen.</li>
  <li>You may click the up/down arrows by any column to re-sort.</li>
  <li>You may type your email in the text field to have a CSV of the chosen department (sorted by the criteria of your choosing) sent to your e-mail.</li>
  <li>You may also click the Download CSV button to be redirected to download the CSV</li>
  </h6>
</ul>

<h5>ALL DEPARTMENTS</h5>
<h6>/all_departments</h6>
  <ul>
    <li>This route redirects you to /departments, automatically populating the all departments option.</li>
  </ul>
 
<h5>Add NEW STAFF:</h5>
<h6>/add_new_staff</h6>
  <ul>
    <li>Enter the required information of a staff member.</li>
    <li>The staff member will be added to the appropriate SQL databases and you will see their information populate in the any of the apporpriate routes.</li>
  </ul>

<h5>REMOVE STAFF:</h5>
<h6>/remove_staff</h6>
  <ul>
   <li>A manager PIN is typically required to remove a staff member. However, for this demo, you may use '0000' to test this feature out!</li>
   <li>Once a staff member is removed, their information is added to a former_staff database, which you can access from the /former_staff route</li>
  </ul>
   

<h5>STAFF_LOOKUP:</h5>
<h6>/staff_lookup</h6>
  <ul>
  ` <li>This route allows you type in partial information to find any staff member.</li>
    <li>(i.e. if 'ar' is typed in the text field and 'First Name' is selected from the dropdown menu, all staff members with 'ar' anywhere in their first name will be displayed).</li>
   `<li>All staff members who match the search criteria will populate</li>
  </ul>
   
<h5>EDIT STAFF:</h5>
<h6>/edit_staff</h6>
  
  <ul>
    <li>This route allows you to edit any of the staff information</li>
    <li>First search for the staff member you wish to edit, using a similar method to staff_lookup (typing partial information will display all matchin results)</li>
    <li>Next, select the staff member you wish to edit.</li>
    <li>Last, select the item you wish to edit and type in the new value you wish to assign to that item.</li>
  </ul>
   
<h5>SALARY:</h5>
<h6>/salary</h6>
  <ul>
    <li>This route simply displays a table of all staff members and their corresponding salaries.</li>
  </ul>
  
