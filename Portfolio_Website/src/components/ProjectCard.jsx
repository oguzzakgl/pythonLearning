import React from 'react';
import { motion } from 'framer-motion';
import { Github } from 'lucide-react';

const ProjectCard = ({ project, index }) => {
    const Icon = project.icon;

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: index * 0.1 }}
            className="group relative bg-[#121212] border border-white/5 rounded-2xl overflow-hidden shadow-xl hover:shadow-primary/20 transition-all duration-300"
        >
            {/* Image Overlay */}
            <div className="relative h-48 overflow-hidden">
                <div className="absolute inset-0 bg-dark/20 group-hover:bg-transparent transition-colors z-10" />
                <img
                    src={project.image}
                    alt={project.title}
                    className="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500"
                />
            </div>

            <div className="p-6 relative z-20 -mt-8">
                <div className="mb-4 inline-block p-3 bg-dark border border-white/10 rounded-xl shadow-lg group-hover:border-primary/50 transition-colors">
                    <Icon size={24} className="text-white group-hover:text-primary transition-colors" />
                </div>

                <h3 className="text-xl font-bold text-white mb-2 group-hover:text-primary transition-colors">{project.title}</h3>
                <p className="text-gray-400 text-sm mb-6 line-clamp-3">{project.description}</p>

                <div className="flex flex-wrap gap-2 mb-6">
                    {project.tags.slice(0, 3).map(tag => (
                        <span key={tag} className="text-xs px-2 py-1 bg-white/5 border border-white/10 rounded-md text-gray-400">
                            {tag}
                        </span>
                    ))}
                    {project.tags.length > 3 && (
                        <span className="text-xs px-2 py-1 bg-white/5 border border-white/10 rounded-md text-gray-400">
                            +{project.tags.length - 3}
                        </span>
                    )}
                </div>

                <a
                    href={project.githubLink}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center text-sm font-medium text-white bg-white/10 px-4 py-2 rounded-lg hover:bg-white/20 transition-all border border-white/10 gap-2 w-full justify-center"
                >
                    <Github size={16} />
                    GitHub'da Gör
                </a>
            </div>
        </motion.div>
    );
};

export default ProjectCard;
