const express = require('express');
const router = express.Router();

// Controller
const {{component_name}} = require('./controller.js');

// GET /{{component_name}}
router.get('/', {{component_name}}.find);

// GET /{{component_name}}/:id
router.get('/:id', {{component_name}}.findById);

// POST /{{component_name}}
router.post('/', {{component_name}}.save);

// PUT /{{component_name}}/:id
router.put('/:id', {{component_name}}.update);

// DELETE /{{component_name}}/:id
router.delete('/:id', {{component_name}}.delete);

module.exports = router;
