import React, { useEffect, useState, useRef } from "react";
import AOS from "aos";
import "aos/dist/aos.css"; // Import AOS CSS
import "../styles/ImageItem.css"; // Import custom CSS
import image1 from "../assets/images.jpg"; // Import image1
import image2 from "../assets/images (1).jpg"; // Import image2

const ImageItem = () => {
  const [firstImageLoaded, setFirstImageLoaded] = useState(false);
  const [secondImageVisible, setSecondImageVisible] = useState(true); // Set to true initially
  const secondImageRef = useRef(null);

  useEffect(() => {
    AOS.init({ duration: 2000 }); // Initialize AOS with options

    // Add appear class to first image after a delay
    setTimeout(() => {
      setFirstImageLoaded(true);
    }, 1000); // Adjust delay as needed

    // Intersection Observer to track visibility of second image
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setSecondImageVisible(true);
          } else {
            setSecondImageVisible(false);
          }
        });
      },
      { threshold: 0.5 } // Trigger when 50% of the image is visible
    );

    if (secondImageRef.current) {
      observer.observe(secondImageRef.current);
    }

    // Clean up observer
    return () => {
      if (secondImageRef.current) {
        observer.unobserve(secondImageRef.current);
      }
    };
  }, []);

  return (
    <div className={`image ${firstImageLoaded ? "appear" : ""}`}>
      <div className="aos-init aos animate" data-aos="fade-left">
        <img src={image1} alt="image1" className="half-image" />
      </div>

      <div className="image-container">
        <img
          ref={secondImageRef}
          src={image2}
          alt="image2"
          className={`half-image2 ${secondImageVisible ? "appear" : ""}`}
          data-aos="fade-left"
        />
      </div>
    </div>
  );
};

export default ImageItem;
