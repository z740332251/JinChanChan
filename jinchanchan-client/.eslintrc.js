// .eslintrc.js example
module.exports = {
    "env": {
        "browser": true,
        "es2021": true
    },
    "extends": "eslint:recommended",
    "parserOptions": {
        "ecmaVersion": "latest",
        "sourceType": "module"
    },
    rules: {
        "no-unused-vars": ["warn", { "vars": "all", "args": "after-used", "ignoreRestSiblings": true }]
    },
  }