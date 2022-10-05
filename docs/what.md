```{include} _templates/nav.html
```

# What you will make

This tutorial will guide you through creating a custom Django administration panel
where reporters can inspect, edit and augment a list of invitees to the [Academy of
Motion Picture Arts and Sciences](http://www.oscars.org/), the elite organization that decides the Oscars.

```{image} /_static/hello-admin-filter.png
```

In 2012, [a study by the Los Angeles Times](http://www.latimes.com/entertainment/movies/academy/la-et-unmasking-oscar-academy-project-html-htmlstory.html) found that the group is overwhelmingly white and male, which led to renewed calls to diversify the Oscar voting pool. A new list was used to write [a follow-up story](http://www.latimes.com/entertainment/envelope/moviesnow/la-et-mn-diversity-oscar-academy-members-20131221-story.html) in 2013. The analysis appeared on the front page [again in early 2015](http://www.latimes.com/entertainment/movies/la-et-mn-oscar-nominations-diversity-20150116-story.html#page=1) when the academy
was criticized after announcing a [virtually all-white slate](http://graphics.latimes.com/oscar-nominees-2015/) of nominees.

In the steps below, you will repeat The Times' work using the academy's 2014 invitation list,
creating a system to share the load of producing a follow-up story in [the vein of this 2016 update to the original analysis](http://graphics.latimes.com/oscars-2016-voters/).

You are following in the footsteps of Times reporters [Sandra Poindexter](http://www.latimes.com/la-bio-sandra-poindexter-staff.html) and [Doug Smith](http://www.latimes.com/la-bio-doug-smith-staff.html), who developed a similar administration panel as part of their investigation. They were inspired by a presentation made by [Matt Wynn](http://mattwynn.net/) at a past conference of The National Institute for Computer-Assisted Reporting.