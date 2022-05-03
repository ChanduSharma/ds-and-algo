import { combineReducers } from 'redux';

const songReducers = () => {

    return [
        {
            title: "Summer of 69",
            duration: "4:29"
        },
        {
            title: "Numb",
            duration: "3:23"
        },
        {
            title: "Believer",
            duration: "2:34"
        }
    ];
}

const selectedSongReducer = (selectedSong = null, action) => {

    if (action.type === 'SONG_SELECTED') {
        return action.payload;
    }

    return selectedSong;
}

export default combineReducers({
    songs: songReducers,
    selectedSong: selectedSongReducer
});