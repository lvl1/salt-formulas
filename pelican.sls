python-pelican:
  pkg:
    - installed

markdown:
  pkg:
    - installed

/opt/courses:
  pelican.build_site:
    - output: /usr/share/nginx/html
