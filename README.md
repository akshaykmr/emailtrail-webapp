#### A simple web application for analysing hops taken by an email to reach you.

#### [Demo link](https://emailtrail.oorja.io)
#### Uses the [emailtrail python module](https://github.com/akshayKMR/emailtrail)
#### Screenshots

<img align="center" src="https://i.imgur.com/AQguHJj.png">

<br>

<img align="center" src="https://i.imgur.com/zicQ94L.png">

#### Development

- Fork and clone the repository
- Build container `docker build -t emailtrail .`
- Run Docker container with `docker run --network host emailtrail`
- View `app.py` to know about available api methods

- Frontend:
  - Its a single page app made with vue.js
  - `cd vue-app`
  - Install dependencies: `npm install`
  - Run: `npm run dev` (Keep the api server running on 8080. The dev server will automatically proxy api requests to it.)
