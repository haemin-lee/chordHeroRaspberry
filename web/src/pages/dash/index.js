import { useEffect, useState, useRef } from "react";
import { useSelector } from "react-redux";
import { Row, Col, Container } from "react-bootstrap";
import axios from "axios";
import Button from "react-bootstrap/Button";
import zoom from "./img/zoom.jpg";


function Dash() {
  return (
    <div className="container">
      <h2 style={{ textAlign: "center" }}>Welcome to ChordHero!</h2>
      <p style={{ textAlign: "center" }}>
        Please enter a song you want to hear here!
      </p>

      
    </div>
  );
}

export default Dash;
