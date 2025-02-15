import React, { useState } from 'react';

const HomePg = () => {
    const [playlistLink, setPlaylistLink] = useState('');

    const handleInputChange = (e) => {
        setPlaylistLink(e.target.value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Submitted playlist link:', playlistLink);
        // Add your form submission logic here
    };

    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h1>Enter your Spotify Playlist Link</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={playlistLink}
                    onChange={handleInputChange}
                    placeholder="Enter Spotify Playlist Link"
                    style={{ width: '300px', padding: '10px', fontSize: '16px' }}
                />
                <button type="submit" style={{ marginLeft: '10px', padding: '10px 20px', fontSize: '16px' }}>
                    Submit
                </button>
            </form>
        </div>
    );
};

export default HomePg;