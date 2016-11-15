---
layout: post
title: Notebook Attempt
date: 2016-11-14
tags:
    - python
    - notebook
--- 
# Can I publish a notebook blog post?

I'm following [Christopher Corley's walkthrough](http://christop.club/2014/02/21
/blogging-with-ipython-and-jekyll/),
[gist](https://gist.github.com/cscorley/9144544), and [this gist from the
comments on that previous
gist](https://gist.github.com/tgarc/7d6901858ef708030c19). 

**In [1]:**

{% highlight python %}
%pylab inline
{% endhighlight %}

    Populating the interactive namespace from numpy and matplotlib


**In [2]:**

{% highlight python %}
fig, ax = plt.subplots()
xs = np.arange(-10, 11, 1)
ys = np.abs(xs)
ax.plot(xs, ys);
{% endhighlight %}

 
![png]({{ BASE_PATH }}/images/2016-11-14-notebook-attempt_2_0.png) 


**In [None]:**

{% highlight python %}

{% endhighlight %}
