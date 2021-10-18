const express = require('express');
const path = require('path');
const app = express();
const bodyParser = require('body-parser');

const personalData = require('./public/data/user_info.json');

app.set('view engine', 'ejs');
app.set('views', 'views');

const _dirname = path.dirname(process.mainModule.filename);

app.use(express.static(path.join(_dirname, "public")));

app.use(bodyParser.urlencoded({
    extended: false
  }));

const projects =  [
    {
        name: "Secure Password Generator",
        githubUrl: "https://github.com/JusWes16/personal-protfolio/tree/master/password-generator",
        language: "Python"
    },
    {
        name: "Space Invaders Clone",
        githubUrl: "https://github.com/JusWes16/cse210-project",
        language: "Python"
    },
    {
        name: "Shop Project",
        githubUrl: "https://github.com/JusWes16/cse341-shop-project",
        language: "JavaScript"
    },
    {
        name: "Rexburg Commons Magazine",
        githubUrl: "https://github.com/Alexander-Mestre/RexburgCommonsMagazine",
        language: "JavaScript"
    },
    {
        name: "PHP Motors",
        githubUrl: "https://github.com/JusWes16/finalproject",
        language: "PHP"
    }
];


app.get('/', (req, res) => {
    console.log('Home Page');
    res.render('index', {
        pageTitle: 'Portfolio | Home',
        path: '/',
        data: personalData
    });
});

app.get('/projects', (req, res) => {
    console.log('Projects Page');
    res.render('projects', {
        pageTitle: 'Portfolio | Projects',
        path: '/projects',
        data: personalData,
        projects: projects
    });
});

app.post('/projects-searched', (req, res) => {
    console.log('Projects Page');
    const search = req.body.searched;

    let searched_projects = [];
    projects.forEach(project => {
        if(project.language.toLowerCase() === search.toLowerCase()){
            searched_projects.push(project);
        } else if(search.toLowerCase() === "all") {
            searched_projects = projects
        }
    });
    res.render('projects', {
        pageTitle: 'Portfolio | Projects',
        path: '/projects',
        data: personalData,
        projects: searched_projects
    });
});

app.get('/about', (req, res) => {
    console.log('About Page');
    res.render('about', {
        pageTitle: 'Portfolio | About',
        path: '/about',
        data: personalData
    });
});
const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Listening on port ${port}...`));