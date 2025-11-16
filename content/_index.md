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
        
        <br> <br> <br>
        
        **We're hiring for research scientists and research associates!** Our team is looking to recruit predoctoral and postdoctoral researchers with backgrounds in natural language processing, computer vision, behavioral sciences, and machine learning. [Apply here](mailto:applytomdsr@adobe.com) to join our team.
        
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
      title: Latest News
      text: ""
      count: 5
      filters:
        folders:
          - post
    design:
      view: compact
      columns: '1'

  - block: collection
    content:
      title: Publications
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'conference'
    design:
      view: citation-custom
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
