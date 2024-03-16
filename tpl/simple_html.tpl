<!DOCTYPE html>

<head>
    <meta charset="utf-8">
</head>

<body>
    {% set identity = root.find('identity') -%}
    <h1>{{ identity.find('name').text }}'s resumé</h1>

    {% set contact = root.find('contact') -%}
    {% set email = contact.find('email') -%}
    <p>You can contact me through my {{ email.get('type') }} email: {{ email.text }}</p>

    {% set skills = root.find('skills') -%}
    My skills include:
    <ul>
        {% for skill in skills.findall('skill') -%}
        <li>The {{ {"proglang": "programming language",
                    "tech": "technology",
                    "language": "spoken language of",
                    "soft": "soft skill of"}[skill.get('type')] 
            }} {{ skill.text }}</li>
        {% endfor %}
    </ul>
<body>
