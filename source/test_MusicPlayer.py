from MusicPlayer import MusicPlayer

screen = 1 # dummy screen

def test_can_get_audio_file_path():
    music_player = MusicPlayer(screen)
    valid_file = 'A/Valid/Directory/And/File/test.mp3'
    assert music_player.getAudioFilePath(123) == None # integer test
    assert music_player.getAudioFilePath(7.1) == None # float test
    assert music_player.getAudioFilePath('test.wav') == None # .wav file
    assert music_player.getAudioFilePath('test.mp4') == None # .mp4 file
    assert music_player.getAudioFilePath('.mp3.wav') == None # .wav file named .mp3
    assert music_player.getAudioFilePath(valid_file) == valid_file # valid file test

    
