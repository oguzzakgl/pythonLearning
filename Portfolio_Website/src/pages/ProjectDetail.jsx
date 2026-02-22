import React, { useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { projects } from '../data/projects';
import { motion } from 'framer-motion';
import { Github, ArrowLeft } from 'lucide-react';
import Footer from '../components/Footer';

const ProjectDetail = () => {
    const { id } = useParams();
    const project = projects.find(p => p.id === id);

    useEffect(() => {
        window.scrollTo(0, 0);
    }, [id]);

    if (!project) {
        return <div className="min-h-screen flex items-center justify-center text-white">Proje bulunamadı</div>;
    }

    const Icon = project.icon;

    return (
        <div className="min-h-screen bg-dark text-white">
            {/* Hero Banner */}
            <div className="relative h-[60vh] overflow-hidden">
                <div className="absolute inset-0 bg-gradient-to-t from-dark to-transparent z-10" />
                <img
                    src={project.image}
                    alt={project.title}
                    className="w-full h-full object-cover object-center"
                />

                {/* Removed "Back to Projects" button as per previous edit, checking if user wants it back? User said 'sol üstteki projelere geç butonu calısmıyor onu kaldır', so keeping it removed. */}

                <div className="absolute bottom-0 left-0 w-full z-20 pb-20 pt-32 bg-gradient-to-t from-dark via-dark/80 to-transparent">
                    <div className="max-w-7xl mx-auto px-6">
                        <motion.div
                            initial={{ opacity: 0, y: 30 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ duration: 0.6 }}
                        >
                            <div className="flex items-center space-x-4 mb-4">
                                <div className="p-3 bg-primary/20 backdrop-blur-md rounded-xl text-primary border border-primary/30">
                                    <Icon size={32} />
                                </div>
                                <span className="px-3 py-1 bg-white/10 rounded-full text-sm font-medium tracking-wide border border-white/10">
                                    {project.category}
                                </span>
                            </div>

                            <h1 className="text-4xl md:text-6xl font-bold mb-6">{project.title}</h1>

                            <div className="flex flex-wrap gap-4">
                                <a href={project.githubLink} className="px-6 py-3 bg-white/10 hover:bg-white/20 text-white rounded-lg font-medium flex items-center space-x-2 transition-all border border-white/10">
                                    <Github size={20} />
                                    <span>Kaynak Kodu</span>
                                </a>
                            </div>
                        </motion.div>
                    </div>
                </div>
            </div>

            {/* Content */}
            <div className="max-w-7xl mx-auto px-6 py-20 grid grid-cols-1 md:grid-cols-3 gap-16">

                {/* Main Info */}
                <div className="md:col-span-2 space-y-12">
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                    >
                        <h2 className="text-2xl font-bold mb-4 flex items-center gap-2">
                            <span className="w-8 h-1 bg-primary rounded-full" /> Proje Özeti
                        </h2>
                        <p className="text-gray-300 text-lg leading-relaxed whitespace-pre-line">
                            {project.description}
                        </p>
                    </motion.div>
                </div>

                {/* Sidebar Cards */}
                <div className="space-y-8">
                    {/* Tech Stack Card */}
                    <motion.div
                        initial={{ opacity: 0, x: 20 }}
                        whileInView={{ opacity: 1, x: 0 }}
                        viewport={{ once: true }}
                        className="p-6 bg-[#121212] border border-white/5 rounded-2xl"
                    >
                        <h3 className="text-xl font-bold mb-4">Teknolojiler</h3>
                        <div className="flex flex-wrap gap-2">
                            {project.tags.map(tag => (
                                <span key={tag} className="px-3 py-1 bg-white/5 border border-white/10 rounded-lg text-sm text-gray-300">
                                    {tag}
                                </span>
                            ))}
                        </div>
                    </motion.div>
                </div>
            </div>

            <Footer />
        </div>
    );
};

export default ProjectDetail;
