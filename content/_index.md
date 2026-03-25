---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        About
      image:
        filename: icon.png
      text: |
        <br>
        The MDSR Lab is a group of researchers committed to solving hard problems in the broad area of digital media and marketing. The group develops cutting-edge machine learning approaches for important use cases including content understanding and generation, behavior modeling, and human-computer interaction.
        
  # - block: markdown
  #   content:
  #     title:
  #     subtitle: ''
  #     text:
  #   design:
  #     columns: '1'
  #     background:
  #       image: 
  #         filename: coders.jpg
  #         filters:
  #           brightness: 1
  #         parallax: false
  #         position: center
  #         size: cover
  #         text_color_light: true
  #     spacing:
  #       padding: ['20px', '0', '20px', '0']
  #     css_class: fullscreen

  - block: collection
    content:
      title: Impact
      text: ""
      count: 5
      filters:
        folders:
          - impact
    design:
      view: impact-citation
      columns: '1'

  - block: collection
    content:
      title: Research
      text: ""
      count: 5
      filters:
        folders:
          - research
        publication_type: 'conference'
      archive:
        enable: true
        link: research/
    design:
      view: citation-custom
      columns: '1'
---
