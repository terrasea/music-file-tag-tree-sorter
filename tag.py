# tag.py
#
# Copyright (C) 2011 - Unknown
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from mutagen import File

class TagTypeError(Exception):
    def __init__(self):
        super(TagTypeError, self).__init__ ("Unknown file tag type")
        

class Tag(object):
    def __init__(self, filename):
        self.tags = File(filename, easy=True)
        if self.tags == None:
            raise TagTypeError()

    @property
    def album(self):
        return self.tags.get('album')

    @album.setter
    def album(self, value):
        self.tags['album'] = value

    @album.deleter
    def album(self):
        del self.tags['album']

    @property
    def artist(self):
        return self.tags.get('artist')

    @artist.setter
    def artist(self, value):
        self.tags['artist'] = value

    @artist.deleter
    def artist(self):
        del self.tags['artist']


    @property
    def title(self):
        return self.tags.get('title')

    @title.setter
    def title(self, value):
        self.tags['title'] = value

    @title.deleter
    def title(self):
        del self.tags['title']


    @property
    def track(self):
        return self.tags.get('tracknumber')

    @track.setter
    def track(self, value):
        self.tags['tracknumber'] = value

    @track.deleter
    def track(self):
        del self.tags['tracknumber']

    def save(self):
        self.tags.save();


if __name__ == "__main__":
    import unittest

    OGGFILE = "test.ogg"
    MP3FILE = "test.mp3"
    
    class TestOggTag(unittest.TestCase):
        def setUp(self):
            self.tag = Tag(OGGFILE)

        def test_get_album(self):
            self.assertEqual(self.tag.album, [u'album'])

        def test_set_album(self):
            self.tag.album = 'new album'
            self.assertEqual(self.tag.album, [u'new album'])


        def test_del_album(self):
            del self.tag.album
            self.assertEqual(self.tag.album, None)
            
        def test_get_artist(self):
            self.assertEqual(self.tag.artist, [u'artist'])

        def test_set_artist(self):
            self.tag.artist = 'new artist'
            self.assertEqual(self.tag.artist, [u'new artist'])


        def test_del_artist(self):
            del self.tag.artist
            self.assertEqual(self.tag.artist, None)

            
        def test_get_title(self):
            self.assertEqual(self.tag.title, [u'title'])

        def test_set_title(self):
            self.tag.title = 'new title'
            self.assertEqual(self.tag.title, [u'new title'])


        def test_del_title(self):
            del self.tag.title
            self.assertEqual(self.tag.title, None)


        def test_get_track(self):
            self.assertEqual(self.tag.track, [u'1'])

        def test_set_track(self):
            self.tag.track = '2'
            self.assertEqual(self.tag.track, [u'2'])


        def test_del_track(self):
            del self.tag.track
            self.assertEqual(self.tag.track, None)
            
            
        def test_save(self):
            self.tag.album = 'album'
            self.tag.artist = 'artist'
            self.tag.title = 'title'
            self.tag.track = '1'
            self.tag.save()
            tag2 = Tag(OGGFILE)
            self.assertEqual(self.tag.tags, tag2.tags)

        def tearDown (self):
            self.tag.album = 'album'
            self.tag.artist = 'artist'
            self.tag.title = 'title'
            self.tag.track = '1'
            self.tag.save()


    class TestMp3Tag(unittest.TestCase):
        def setUp(self):
            self.tag = Tag(MP3FILE)

        def test_get_album(self):
            self.assertEqual(self.tag.album, [u'album'])

        def test_set_album(self):
            self.tag.album = 'new album'
            self.assertEqual(self.tag.album, [u'new album'])


        def test_del_album(self):
            del self.tag.album
            self.assertEqual(self.tag.album, None)
            
        def test_get_artist(self):
            self.assertEqual(self.tag.artist, [u'artist'])

        def test_set_artist(self):
            self.tag.artist = 'new artist'
            self.assertEqual(self.tag.artist, [u'new artist'])


        def test_del_artist(self):
            del self.tag.artist
            self.assertEqual(self.tag.artist, None)

            
        def test_get_title(self):
            self.assertEqual(self.tag.title, [u'title'])

        def test_set_title(self):
            self.tag.title = 'new title'
            self.assertEqual(self.tag.title, [u'new title'])


        def test_del_title(self):
            del self.tag.title
            self.assertEqual(self.tag.title, None)


        def test_get_track(self):
            self.assertEqual(self.tag.track, [u'1'])

        def test_set_track(self):
            self.tag.track = '2'
            self.assertEqual(self.tag.track, [u'2'])


        def test_del_track(self):
            del self.tag.track
            self.assertEqual(self.tag.track, None)
            
            
        def test_save(self):
            self.tag.album = 'album'
            self.tag.artist = 'artist'
            self.tag.title = 'title'
            self.tag.track = '1'
            self.tag.save()
            tag2 = Tag(MP3FILE)
            self.assertEqual(self.tag.tags, tag2.tags)

        def tearDown (self):
            self.tag.album = 'album'
            self.tag.artist = 'artist'
            self.tag.title = 'title'
            self.tag.track = '1'
            self.tag.save()

    unittest.main()
    
    