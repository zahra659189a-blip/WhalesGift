// ═══════════════════════════════════════════════════════════════
// 📢 CHANNELS VERIFICATION SYSTEM
// ═══════════════════════════════════════════════════════════════

async function checkRequiredChannels() {
    try {
        // Get required channels from backend
        const response = await fetch(`${CONFIG.API_BASE_URL}/admin/channels`);
        const result = await response.json();
        
        if (!result.success || !result.data || result.data.length === 0) {
            // No required channels, proceed normally
            console.log('📢 No required channels configured');
            return true;
        }
        
        const channels = result.data;
        console.log('📢 Found required channels:', channels.length);
        
        // Check if user has verified channels before (using localStorage)
        const userId = TelegramApp.getUserId() || 'guest';
        const verifiedKey = `channels_verified_${userId}`;
        const lastVerified = localStorage.getItem(verifiedKey) || '0';
        const now = Date.now();
        
        // Check every 24 hours
        if (now - parseInt(lastVerified) < 24 * 60 * 60 * 1000) {
            console.log('📢 User already verified within 24 hours');
            return true;
        }
        
        // Show channels modal
        console.log('📢 Showing channels verification modal');
        await showChannelsModal(channels);
        
        return true;
        
    } catch (error) {
        console.error('Error checking channels:', error);
        // Don't block user if there's an error
        return true;
    }
}

async function showChannelsModal(channels) {
    return new Promise((resolve) => {
        const modal = document.getElementById('channels-modal');
        const channelsList = document.getElementById('channels-list');
        const verifyBtn = document.getElementById('verify-channels-btn');
        
        // Store subscription status for each channel
        const channelStatus = {};
        channels.forEach(channel => {
            channelStatus[channel.channel_id] = false;
        });
        
        // Build channels list
        const renderChannels = () => {
            channelsList.innerHTML = '';
            channels.forEach(channel => {
                const isSubscribed = channelStatus[channel.channel_id];
                const channelItem = document.createElement('div');
                channelItem.className = 'channel-item';
                channelItem.dataset.channelId = channel.channel_id;
                channelItem.innerHTML = `
                    <div class="channel-info">
                        <svg class="channel-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path>
                        </svg>
                        <div>
                            <div class="channel-name">${channel.channel_name}</div>
                            <div class="channel-id">${channel.channel_id}</div>
                        </div>
                    </div>
                    <div class="channel-actions">
                        <a href="${channel.channel_url}" target="_blank" class="channel-join-btn" onclick="markChannelAsOpened('${channel.channel_id}')">
                            📢 ${channel.channel_name}
                        </a>
                        <span class="channel-status ${isSubscribed ? 'subscribed' : 'not-subscribed'}">
                            ${isSubscribed ? '✅' : '❌'}
                        </span>
                    </div>
                `;
                channelsList.appendChild(channelItem);
            });
        };
        
        // Mark channel as opened when user clicks the link
        window.markChannelAsOpened = (channelId) => {
            TelegramApp.hapticFeedback('light');
            setTimeout(() => {
                channelStatus[channelId] = true;
                renderChannels();
            }, 1000);
        };
        
        renderChannels();
        
        // Show modal
        modal.style.display = 'flex';
        
        // Handle verify button
        verifyBtn.onclick = async () => {
            TelegramApp.hapticFeedback('medium');
            verifyBtn.disabled = true;
            verifyBtn.textContent = '⏳ جاري التحقق...';
            
            // Check if all channels are marked as visited
            const allSubscribed = Object.values(channelStatus).every(status => status === true);
            
            if (!allSubscribed) {
                verifyBtn.disabled = false;
                verifyBtn.textContent = '✅ تحقق من الاشتراك';
                showToast('⚠️ يرجى الاشتراك في جميع القنوات أولاً', 'error');
                TelegramApp.hapticFeedback('error');
                return;
            }
            
            // Simulate verification delay
            await new Promise(r => setTimeout(r, 1500));
            
            // Mark as verified
            const userId = TelegramApp.getUserId() || 'guest';
            const verifiedKey = `channels_verified_${userId}`;
            localStorage.setItem(verifiedKey, Date.now().toString());
            
            // Close modal
            modal.style.display = 'none';
            showToast('✅ تم التحقق من الاشتراك بنجاح!', 'success');
            TelegramApp.hapticFeedback('success');
            
            resolve(true);
        };
    });
}
