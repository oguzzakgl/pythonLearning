import React from 'react';
import HeroSection from '../components/HeroSection';
import AboutSection from '../components/AboutSection';
import ProjectCard from '../components/ProjectCard';
import Footer from '../components/Footer';
import { projects } from '../data/projects';
import { motion } from 'framer-motion';

const Home = () => {
    return (
        <div className="min-h-screen bg-dark">
            <HeroSection />
            <AboutSection />

            <section id="projects" className="py-20 relative z-10">
                <div className="max-w-7xl mx-auto px-6">
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        className="mb-12"
                    >
                        <h2 className="text-4xl font-bold text-white mb-4">Öne Çıkan Projeler</h2>
                        <p className="text-gray-400 max-w-2xl">
                            Python, Veri Bilimi ve Modern Web Teknolojileri kullanarak geliştirdiğim seçilmiş projeler.
                        </p>
                    </motion.div>
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-8">
                        {projects.map((project, index) => (
                            <ProjectCard key={project.id} project={project} index={index} />
                        ))}
                    </div>
                </div>
            </section>

            <Footer />
        </div>
    );
};

export default Home;
