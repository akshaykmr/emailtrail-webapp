# A simple web application for analysing an email trail

### Work in progress

### What information can I expect?
> Hostname, Protocol, Timestamp and Delay for each Hop.

### Uses the [emailtrail python module](https://github.com/akshayKMR/emailtrail)


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