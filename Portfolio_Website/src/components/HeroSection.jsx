import React from 'react';
import { motion } from 'framer-motion';
import { ArrowRight, Mail, Github, Linkedin, Download } from 'lucide-react';

const HeroSection = () => {
    return (
        <div className="relative min-h-screen flex items-center justify-center pt-20 overflow-hidden">
            {/* Background Abstract Effects */}
            <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[600px] bg-primary/20 blur-[120px] rounded-full pointer-events-none" />
            <div className="absolute bottom-0 right-0 w-[600px] h-[400px] bg-dark-to/40 blur-[100px] rounded-full pointer-events-none" />

            <div className="max-w-7xl mx-auto px-6 relative z-10 w-full grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
                {/* Left: Personal Info */}
                <motion.div
                    initial={{ opacity: 0, x: -50 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ duration: 0.8, ease: "easeOut" }}
                >
                    <h1 className="text-5xl md:text-7xl font-bold leading-tight text-white mb-6">
                        Oğuz Kaan Akgül
                    </h1>

                    <p className="text-2xl md:text-3xl text-primary font-medium mb-8">
                        Bilgisayar Mühendisliği 4. Sınıf Öğrencisi
                    </p>

                    <div className="flex flex-wrap gap-3">
                        <a href="#projects" className="group px-8 py-3 bg-primary hover:bg-primary-glow text-white rounded-full font-medium transition-all shadow-lg shadow-primary/25 flex items-center space-x-2">
                            <span>Projelerimi Gör</span>
                            <ArrowRight size={18} className="group-hover:translate-x-1 transition-transform" />
                        </a>
                        <a
                            href="/oguzCV.pdf"
                            download="Oguz_Kaan_Akgul_CV.pdf"
                            className="group px-8 py-3 bg-white/5 border border-white/10 hover:bg-primary/20 hover:border-primary/50 text-white rounded-full font-medium transition-all flex items-center space-x-2"
                        >
                            <Download size={18} className="group-hover:-translate-y-0.5 transition-transform" />
                            <span>CV İndir</span>
                        </a>
                        <a href="#contact" className="px-8 py-3 bg-white/5 border border-white/10 hover:bg-white/10 text-white rounded-full font-medium transition-all flex items-center space-x-2">
                            <Mail size={18} />
                            <span>Bana Ulaş</span>
                        </a>
                    </div>
                </motion.div>

                {/* Right: Contact Cards */}
                <motion.div
                    initial={{ opacity: 0, scale: 0.9 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ duration: 0.8, delay: 0.2 }}
                    className="relative hidden md:flex flex-col gap-6 items-center justify-center"
                >
                    {/* GitHub Card */}
                    <a
                        href="https://github.com/oguzzakgl"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="w-full max-w-sm p-4 bg-[#1e1e1e]/50 backdrop-blur-md border border-white/10 rounded-2xl flex items-center gap-4 hover:bg-white/5 hover:border-primary/50 transition-all group"
                    >
                        <div className="p-3 bg-white/5 rounded-xl group-hover:bg-primary/20 transition-colors">
                            <Github size={32} className="text-white group-hover:text-primary" />
                        </div>
                        <div>
                            <h3 className="text-white font-bold">GitHub</h3>
                            <p className="text-gray-400 text-sm group-hover:text-primary/80">github.com/oguzzakgl</p>
                        </div>
                    </a>

                    {/* LinkedIn Card */}
                    <a
                        href="https://linkedin.com/in/oguzkaanakgul00"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="w-full max-w-sm p-4 bg-[#1e1e1e]/50 backdrop-blur-md border border-white/10 rounded-2xl flex items-center gap-4 hover:bg-white/5 hover:border-primary/50 transition-all group"
                    >
                        <div className="p-3 bg-white/5 rounded-xl group-hover:bg-primary/20 transition-colors">
                            <Linkedin size={32} className="text-white group-hover:text-primary" />
                        </div>
                        <div>
                            <h3 className="text-white font-bold">LinkedIn</h3>
                            <p className="text-gray-400 text-sm group-hover:text-primary/80">linkedin.com/in/oguzkaanakgul00</p>
                        </div>
                    </a>

                    {/* Mail Card */}
                    <a
                        href="mailto:oguzzakg@gmail.com"
                        className="w-full max-w-sm p-4 bg-[#1e1e1e]/50 backdrop-blur-md border border-white/10 rounded-2xl flex items-center gap-4 hover:bg-white/5 hover:border-primary/50 transition-all group"
                    >
                        <div className="p-3 bg-white/5 rounded-xl group-hover:bg-primary/20 transition-colors">
                            <Mail size={32} className="text-white group-hover:text-primary" />
                        </div>
                        <div>
                            <h3 className="text-white font-bold">E-Posta</h3>
                            <p className="text-gray-400 text-sm group-hover:text-primary/80">oguzzakg@gmail.com</p>
                        </div>
                    </a>

                </motion.div>
            </div>
        </div>
    );
};

export default HeroSection;
