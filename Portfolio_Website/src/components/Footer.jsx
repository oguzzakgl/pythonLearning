import React from 'react';
import { Github, Linkedin, Mail } from 'lucide-react';

const Footer = () => {
    return (
        <footer className="bg-[#050505] border-t border-white/5 py-12 relative z-10" id="contact">
            <div className="max-w-7xl mx-auto px-6 flex justify-center items-center">
                {/* Socials */}
                <div className="flex space-x-6">
                    <a href="https://github.com/oguzzakgl" target="_blank" rel="noopener noreferrer" className="p-3 bg-white/5 rounded-full text-gray-400 hover:text-white hover:bg-white/10 transition-all hover:scale-110">
                        <Github size={24} />
                    </a>
                    <a href="https://linkedin.com/in/oguzkaanakgul00" target="_blank" rel="noopener noreferrer" className="p-3 bg-white/5 rounded-full text-gray-400 hover:text-white hover:bg-white/10 transition-all hover:scale-110">
                        <Linkedin size={24} />
                    </a>
                    <a href="mailto:oguzzakg@gmail.com" className="p-3 bg-white/5 rounded-full text-gray-400 hover:text-white hover:bg-white/10 transition-all hover:scale-110">
                        <Mail size={24} />
                    </a>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
