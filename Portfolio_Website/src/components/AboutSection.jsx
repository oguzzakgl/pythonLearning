import React from 'react';
import { motion } from 'framer-motion';

const AboutSection = () => {
    const techs = [
        { name: 'Python', color: 'bg-blue-500/10 text-blue-400 border-blue-500/20' },
        { name: 'Pandas', color: 'bg-purple-500/10 text-purple-400 border-purple-500/20' },
        { name: 'NumPy', color: 'bg-blue-400/10 text-blue-300 border-blue-400/20' },
        { name: 'Scikit-learn', color: 'bg-orange-500/10 text-orange-400 border-orange-500/20' },
        { name: 'Streamlit', color: 'bg-red-500/10 text-red-400 border-red-500/20' },
        { name: 'Plotly', color: 'bg-indigo-500/10 text-indigo-400 border-indigo-500/20' },
        { name: 'Seaborn', color: 'bg-teal-500/10 text-teal-400 border-teal-500/20' },
        { name: 'Matplotlib', color: 'bg-pink-500/10 text-pink-400 border-pink-500/20' },
        { name: 'FastAPI', color: 'bg-green-600/10 text-green-400 border-green-600/20' },
        { name: 'PostgreSQL', color: 'bg-sky-500/10 text-sky-400 border-sky-500/20' },
        { name: 'SQLite', color: 'bg-slate-500/10 text-slate-400 border-slate-500/20' },
        { name: 'Faker', color: 'bg-yellow-500/10 text-yellow-400 border-yellow-500/20' },
        { name: 'Docker', color: 'bg-blue-600/10 text-blue-400 border-blue-600/20' },
        { name: 'Git', color: 'bg-red-600/10 text-red-400 border-red-600/20' },
    ];

    return (
        <section id="about" className="py-20 relative z-10">
            <div className="max-w-7xl mx-auto px-6">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-16">

                    {/* Left: About Me */}
                    <motion.div
                        initial={{ opacity: 0, x: -30 }}
                        whileInView={{ opacity: 1, x: 0 }}
                        viewport={{ once: true }}
                    >
                        <h2 className="text-3xl font-bold text-white mb-6 flex items-center gap-2">
                            <span className="w-8 h-1 bg-primary rounded-full" /> Hakkımda
                        </h2>
                        <div className="space-y-4 text-gray-400 leading-relaxed">
                            <p>
                                Merhaba! Ben Oğuz Kaan Akgül. Bilgisayar Mühendisliği son sınıf öğrencisi olarak, veri bilimi ve yazılım geliştirme alanlarında kendimi geliştiriyorum.
                            </p>
                            <p>
                                Karmaşık problemleri çözmekten, veriden anlamlı içgörüler çıkarmaktan ve ölçeklenebilir sistemler tasarlamaktan keyif alıyorum. Python ekosistemine (FastAPI, Pandas, Scikit-learn, Streamlit) hakimim ve veri bilimi ile backend geliştirme alanlarında aktif projeler üretiyorum.
                            </p>
                            <p>
                                Sürekli öğrenmeye ve yeni teknolojileri keşfetmeye olan tutkumla, yenilikçi projeler üretmeye odaklanıyorum.
                            </p>
                        </div>
                    </motion.div>

                    {/* Right: Technologies */}
                    <motion.div
                        initial={{ opacity: 0, x: 30 }}
                        whileInView={{ opacity: 1, x: 0 }}
                        viewport={{ once: true }}
                    >
                        <h2 className="text-3xl font-bold text-white mb-6 flex items-center gap-2 md:justify-end">
                            Teknolojiler <span className="w-8 h-1 bg-primary rounded-full order-first md:order-last" />
                        </h2>
                        <div className="flex flex-wrap gap-3 justify-start md:justify-end">
                            {techs.map((tech, index) => (
                                <motion.div
                                    key={tech.name}
                                    initial={{ opacity: 0, scale: 0.8 }}
                                    whileInView={{ opacity: 1, scale: 1 }}
                                    transition={{ delay: index * 0.05 }}
                                    whileHover={{ scale: 1.05 }}
                                    className={`px-4 py-2 rounded-lg border ${tech.color} font-medium cursor-default backdrop-blur-sm`}
                                >
                                    {tech.name}
                                </motion.div>
                            ))}
                        </div>
                    </motion.div>

                </div>
            </div>
        </section>
    );
};

export default AboutSection;
