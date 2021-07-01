"""A video player class."""

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")
 

    def show_all_videos(self):
        """Returns all videos."""
        
        all_videos = self._video_library.get_all_videos()  # Fetch all the videos, based off above function
        all_videos.sort(key=lambda x: x.title)  # Use key with lambda to dictate sort to only go through video title
        print("Here's a list of all available videos:")

        for video in all_videos:  # Loop through txt file, reading each video line by line
            tagString = str(video.tags)  # Convert to string to allow stripping of brackets
            # tagStrip.strip("()") # Old code - this didn't make a difference with this line placement
            print(video.title, "(", video.video_id, ")", "[", tagString.strip("()"), "]")

      #  print("show_all_videos needs implementation")

    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if not video: 
            print ("Error: Video does not exist")
            return
            
        if self._current_video != None: 
            print(f"Stopping video: {self._current_video}")
            print(f"Playing video: {video.title}")
            self._current_video = video.title 
            return 
        
        print(f"Playing Video: {video.title}")
        self._current_video = video.title 
        
    def stop_video(self, video_id):
        """Stops the current video."""

        video = self._video_library.get_video(video_id)
        if video:
            print(f"Stopping video: {video.title}")
            self._current_video = video
        else:
            print("Cannot play video: Video does not exist")

    def play_random_video(self):
        """Plays a random video from the video library."""
        getVideo = self._video_library.get_all_videos()  # Grab all videos
        num_videos = len(self._video_library.get_all_videos())  # Borrowed code to check if videos.txt is empty

        if num_videos == 0:  # Should trigger if there were no videos found in the txt file
            print("There are no videos available to play") # Will need retrofit to fit flagged videos if I get there
        else:
            if self.isPlaying is True:
                print("Stopping video:", self.currentVideo.title)
                self.isPaused = False
            pickVideo = random.choice(getVideo)  # Get Python to pick a random video in the list (must import random)
            print("Playing video:", pickVideo.title)  # Print the video title of what Python picked at random
            self.isPlaying = True  # Borrowed code lines from play_video
            self.currentVideo = pickVideo  # Probably is a way to further streamline this
        #print("play_random_video needs implementation")

    def pause_video(self,video_id):
        """Pauses the current video."""

        video = self._video_library.get_video(video_id)
        if  video:
            print(f'Pause video: {video.title}')
            self._current_video = video
        else:
            print("Cannot play video: Video does not exist")


    def continue_video(self):
        """Resumes playing the current video."""

        if self.video_now is not None:
            if not self.video_paused:
                print(f"Cannot continue video: Video is not paused")
            else:
                print(f"Continuing video: {self.video_now.title}")
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.
        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.
        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.
        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.
        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
