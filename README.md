# GarbageGo

Description: Our Waste Management Website is a modern and scalable platform developed using Python as the primary language for the backend and JavaScript for the frontend. The backend, powered by the Django Rest framework, provides a robust and secure foundation for managing waste-related data and operations. The frontend, built with React, offers a responsive and intuitive user interface.

## Features

- Waste Pickup: Users can schedule pickups for various types of waste materials, including recyclables and non-recyclables. They can specify pickup dates, locations, and provide special instructions.

- Scrap Pickup: Users can request pickups for scrap materials such as metal, electronics, or other recyclable items. They can provide details about the type and quantity of scrap for efficient collection.

- Recycling Information: The website provides valuable information on different waste categories, recycling guidelines, and best practices to encourage users to adopt environmentally-friendly waste management practices.

- User Dashboard: Each user has a personalized dashboard where they can track their waste management activities, view pickup history, and access relevant statistics and reports.

- Rewards and Achievements: The website incentivizes users' recycling efforts by recognizing their accomplishments through badges, achievements, or rewards. Users can earn achievements based on factors such as the weight of recycled materials, consistent recycling, or participation in community events.

- Admin Panel:The Waste Management Website includes a custom admin panel that provides authorized users with access to manage users, pickups, achievements, and other system-related configurations. The custom admin panel offers enhanced functionality and customization options compared to the default Django Admin panel. Administrators can efficiently monitor and administer the waste management system through the custom admin panel.

## Technologies Used

- Django: a high-level Python web framework for rapid development and clean design.
- Django Rest Framework: a powerful and flexible toolkit for building Web APIs.
- PostgreSQL: a powerful, open-source object-relational database system.
- Swagger: a tool for documenting and testing APIs.
- Git: a distributed version control system.

## Getting Started


1. Clone the repository `git clone https://github.com/NithinKrishna10/GarbageGo.git`
2. Navigrate to the working directory `cd garbagego`
3. Open the project from the code editor `code .` or `atom .`
4. Create virtual environment `python -m venv env`
5. Activate the virtual environment `source env/Scripts/activate`
6.Set up the database by configuring the PostgreSQL connection in the project's settings.py file.
7. Create database tables
    ```sh
    python manage.py migrate
    ```
8. Install required packages to run the project `pip install -r requirements.txt`
9. Create a super user
    ```sh
    python manage.py createsuperuser
    ```
    _GitBash users may have to run this to create a super user - `winpty python manage.py createsuperuser`_
10. Run server
    ```sh
    python manage.py runserver

## Contact

For any inquiries or feedback, please contact us at -nithin3119@gmail
com.

