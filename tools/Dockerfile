FROM ubuntu:22.04

# Prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-pygments \
    texlive-latex-base \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-science \
    texlive-extra-utils \
    pandoc \
    git \
    curl \
    pkg-config \
    libcairo2-dev \
    libgirepository1.0-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && \
    pip install bikeshed jsonschema pydantic[email] requests pycairo

# Initialize Bikeshed spec database (this takes time, so cache it in image)
RUN bikeshed update

# Set working directory
WORKDIR /workspace

# Set non-interactive mode for any future package installations
ENV DEBIAN_FRONTEND=

# Default command
CMD ["/bin/bash"]