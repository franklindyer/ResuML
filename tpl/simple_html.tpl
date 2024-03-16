<!DOCTYPE html>

<head>
    <meta charset="utf-8">
</head>

<body>
    {% set identity = resume.find('identity') -%}
    <h1>{{ identity.find('name').text }}'s resumé</h1>

    {% set contact = resume.find('contact') -%}
    {% set email = contact.find('email') -%}
    <p>You can contact me through my {{ email.get('type') }} email: {{ email.text }}</p>

    {% set skills = resume.find('skills') -%}
    My skills include:
    <ul>
        {% for skill in prioritize(skills.findall('skill'), 'skills') -%}
        <li> The {{ {"proglang": "programming language",
                    "tech": "technology",
                    "language": "spoken language of",
                    "soft": "soft skill of"}[skill.get('type')] 
             }} {{ skill.text.strip() }} 
             {%- if skill.find('certification') is not none -%}
             &nbsp;({{ skill.find('certification').text }})
             {%- endif %} </li>
        {% endfor %}
    </ul>
<body>
