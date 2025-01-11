---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: markdown
    content:
      title: We're hiring for research scientists and research associates!
      text: Our team is looking to recruit predoctoral and postdoctoral researchers with backgrounds in natural language processing, computer vision, behavioral sciences, and machine learning.
        {{% cta cta_link="https://adobe.wd5.myworkdayjobs.com/external_experienced/job/Noida/Research-Scientist_R151257-1" cta_text="Apply now →" %}}
    design:
      background:
        color: '#190707'
        text_color_light: true
  
  - block: hero
    content:
      title: |
        Adobe Media and Data Science Research (MDSR) 
        Laboratory
      image:
        filename: welcome.jpg
      text: |
        <br>
        
        The MDSR Lab is a group of researchers committed to solving hard problems in the broad area of digital media and marketing. The group develops cutting-edge machine learning approaches for important use cases including content understanding and generation, behavior modeling, and human-computer interaction.
        
  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: coders.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen

  - block: collection
    content:
      title: Latest Preprints
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
