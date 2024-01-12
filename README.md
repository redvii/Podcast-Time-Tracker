# How to use
Import the package first (ensure you are in the same directory as this package)

```python
import podcast_tracker as pt
```

Then you can start using it.

```python
t = pt.track("mypodcast")
t.note("Hi this is my podcast note")
```

This script will automatically store the notes in your file with the name "mypodcast.csv", along with the timestamp of the note and the time difference since the podcast was initiated using the track() function.