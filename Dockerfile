FROM python:3.12-slim

RUN pip install --no-cache-dir ansible-core

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        openssh-client \
        rsync && \
    rm -rf /var/lib/apt/lists/*

RUN ansible-galaxy collection install \
    ansible.posix \
    community.docker

WORKDIR /work

COPY . /work

# 執行每task會確認
# CMD ["ansible-playbook", "-i", "hosts", "ecx01_install.yml"] 
CMD ["ansible-playbook", "-i", "hosts", "fto01_install.yml"] 