#### A simple web application for analysing hops taken by an email to reach you.

#### [Demo link](https://emailtrail.herokuapp.com)
#### Uses the [emailtrail python module](https://github.com/akshayKMR/emailtrail)
#### Screenshots

<img align="center" src="https://i.imgur.com/AQguHJj.png">

<br>

<img align="center" src="https://i.imgur.com/jrdktzc.png">

#### Development

- Fork and clone the repository
- Install dependencies: `pipenv install --dev`
- View `app.py` to know about available api methods
- Run the api server: `python run.py 8080`
- Frontend:
  - Its a single page app made with vue.js
  - `cd vue-app`
  - Install dependencies: `npm install`
  - Run: `npm run dev` (Keep the api server running on 8080. The dev server will automatically proxy api requests to it.)
