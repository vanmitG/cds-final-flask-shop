# CoderSchool Final Project - _CDS-Ecom-F_

Created with love by: Van Mit

This is a simple e-commerce rest back-end application built using [python and flask](doc/installation.md). A motivation and project brief can be found [on github-gist](https://gist.github.com/vanmitG/9a119a162e6d0390a70d9febdb88f367)

Created with love by: Van Mit

It is currently roughly 30% complete.

## Implemented Stories

- [x] User can performs CRUD on products through api call
- [x] Admin Panel to administer models

## To Be Implemented

- [x] User can login and signup
- [x] User can add, show, delete, update orders
- [x] Sale Admin can only add, update, and delete their products

### Prerequisites

Postgresql should be install on your local system.
Username, user's password, and database' name should be available as showed in these [instructions](doc/setup-postgresql.md)

## Installation Instructions

Clone this repository and run `pip install -r requirements.txt` and/or follow these [instructions](doc/installation.md)

### Deployment

the application can be deployed to Heroku following these [instructions](doc/heroku-deployment.md)

### Database Schema

[An intended database squema](https://www.lucidchart.com/documents/embeddedchart/d1fb31ab-3db5-49e2-b20f-1996423547ff)

### web app demo

[rest backend](#)

### Endpoints

- GET /api/products
- GET /api/products/:id
- POST /api/product
- PUT /api/product/:id
- DELETE /api/product/:id

## Time Spent and Lessons Learned

Time spent: **20** hours spent in total.

Describe any challenges encountered while building the app.

## License

    Copyright ©

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
