import React from 'react';
import './HomePage.css';
import animalGif from '../../assets/images/animalgif.gif';

const HomePage: React.FC = () => {
    return (
        <div className="homepage">
            <h1>Carregando</h1>
            <img src={animalGif} alt="GIF ou Imagem Animada" />
        </div>
    );
};

export default HomePage;
