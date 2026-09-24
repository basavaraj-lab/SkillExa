import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React, { useEffect, useState } from 'react';
import {
  Modal,
  Pressable,
  ScrollView,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import { Palette, Radii, Shadows } from '../constants/theme';
import { CollegeNotification } from '../data/collegeData';
import { CollegeStore } from '../services/collegeStore';
import { useAuth } from './auth-context';

export function CollegeNotificationsModal({ visible, onClose }: { visible: boolean; onClose: () => void }) {
  const { profile } = useAuth();
  const [notifications, setNotifications] = useState<CollegeNotification[]>([]);

  useEffect(() => {
    setNotifications(CollegeStore.getNotifications(profile.id || 'std-101'));
    return CollegeStore.subscribe(() => {
      setNotifications(CollegeStore.getNotifications(profile.id || 'std-101'));
    });
  }, [profile.id]);

  const handleNotificationPress = (notif: CollegeNotification) => {
    CollegeStore.markAsRead(notif.id);
    onClose();
    if (notif.actionRoute) {
      router.push({
        pathname: notif.actionRoute as any,
        params: notif.actionParams,
      });
    }
  };

  const getIcon = (type: CollegeNotification['type']) => {
    switch (type) {
      case 'NOTE':
        return { name: 'file-text', color: Palette.primary };
      case 'QUIZ':
        return { name: 'check-circle', color: Palette.success };
      case 'VIDEO':
        return { name: 'film', color: Palette.aiPurple };
      case 'ASSIGNMENT':
        return { name: 'clipboard', color: Palette.warning };
      case 'INTERVIEW':
        return { name: 'video', color: Palette.danger };
      case 'ANNOUNCEMENT':
      default:
        return { name: 'volume-2', color: Palette.primary };
    }
  };

  return (
    <Modal animationType="fade" transparent visible={visible} onRequestClose={onClose}>
      <Pressable style={styles.backdrop} onPress={onClose}>
        <View style={styles.modalCard} onStartShouldSetResponder={() => true}>
          {/* Header */}
          <View style={styles.header}>
            <View style={styles.titleRow}>
              <Feather name="bell" size={18} color={Palette.primary} />
              <Text style={styles.title}>College Notifications</Text>
            </View>

            <TouchableOpacity onPress={() => CollegeStore.markAllAsRead(profile.id || 'std-101')}>
              <Text style={styles.markAllText}>Mark all as read</Text>
            </TouchableOpacity>
          </View>

          {/* Notifications List */}
          <ScrollView contentContainerStyle={styles.listContent} showsVerticalScrollIndicator={false}>
            {notifications.length === 0 ? (
              <View style={styles.emptyBox}>
                <Feather name="bell-off" size={32} color={Palette.textMuted} />
                <Text style={styles.emptyText}>No notifications yet</Text>
              </View>
            ) : (
              notifications.map((notif) => {
                const iconInfo = getIcon(notif.type);
                return (
                  <TouchableOpacity
                    key={notif.id}
                    style={[styles.itemCard, !notif.isRead && styles.itemCardUnread]}
                    onPress={() => handleNotificationPress(notif)}
                    activeOpacity={0.8}
                  >
                    <View style={[styles.iconBox, { backgroundColor: `${iconInfo.color}15` }]}>
                      <Feather name={iconInfo.name as any} size={16} color={iconInfo.color} />
                    </View>

                    <View style={{ flex: 1 }}>
                      <View style={styles.itemTopRow}>
                        <Text style={styles.itemTitle}>{notif.title}</Text>
                        {!notif.isRead && <View style={styles.unreadDot} />}
                      </View>
                      <Text style={styles.itemMessage}>{notif.message}</Text>
                      <Text style={styles.itemTime}>{notif.createdAt}</Text>
                    </View>
                  </TouchableOpacity>
                );
              })
            )}
          </ScrollView>

          {/* Close Button */}
          <TouchableOpacity style={styles.closeBtn} onPress={onClose}>
            <Text style={styles.closeBtnText}>Close</Text>
          </TouchableOpacity>
        </View>
      </Pressable>
    </Modal>
  );
}

export function NotificationBellButton() {
  const { profile } = useAuth();
  const [unreadCount, setUnreadCount] = useState(0);
  const [modalVisible, setModalVisible] = useState(false);

  useEffect(() => {
    setUnreadCount(CollegeStore.getUnreadCount(profile.id || 'std-101'));
    return CollegeStore.subscribe(() => {
      setUnreadCount(CollegeStore.getUnreadCount(profile.id || 'std-101'));
    });
  }, [profile.id]);

  return (
    <>
      <TouchableOpacity
        style={styles.bellBtn}
        onPress={() => setModalVisible(true)}
        activeOpacity={0.8}
      >
        <Feather name="bell" size={19} color={Palette.textTitle} />
        {unreadCount > 0 && (
          <View style={styles.badge}>
            <Text style={styles.badgeText}>{unreadCount > 9 ? '9+' : unreadCount}</Text>
          </View>
        )}
      </TouchableOpacity>

      <CollegeNotificationsModal visible={modalVisible} onClose={() => setModalVisible(false)} />
    </>
  );
}

const styles = StyleSheet.create({
  bellBtn: {
    width: 38,
    height: 38,
    borderRadius: 12,
    backgroundColor: Palette.backgroundSecondary,
    borderWidth: 1,
    borderColor: Palette.border,
    alignItems: 'center',
    justifyContent: 'center',
    position: 'relative',
  },
  badge: {
    position: 'absolute',
    top: -4,
    right: -4,
    backgroundColor: Palette.danger,
    borderRadius: 9,
    minWidth: 18,
    height: 18,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 4,
    borderWidth: 1.5,
    borderColor: '#FFFFFF',
  },
  badgeText: { color: '#FFFFFF', fontSize: 9.5, fontWeight: '800' },
  backdrop: {
    flex: 1,
    backgroundColor: 'rgba(15, 23, 42, 0.6)',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 18,
  },
  modalCard: {
    width: '100%',
    maxWidth: 420,
    maxHeight: '80%',
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.cardLarge,
    padding: 20,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.floating,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 14,
    paddingBottom: 10,
    borderBottomWidth: 1,
    borderBottomColor: Palette.borderSubtle,
  },
  titleRow: { flexDirection: 'row', alignItems: 'center', gap: 8 },
  title: { fontSize: 16, fontWeight: '800', color: Palette.textTitle },
  markAllText: { fontSize: 11.5, fontWeight: '700', color: Palette.primary },
  listContent: { gap: 10, paddingVertical: 4 },
  itemCard: {
    flexDirection: 'row',
    gap: 12,
    padding: 12,
    borderRadius: Radii.card,
    backgroundColor: Palette.backgroundSecondary,
    borderWidth: 1,
    borderColor: Palette.border,
  },
  itemCardUnread: {
    backgroundColor: '#FFFFFF',
    borderColor: Palette.primaryBorder,
    borderLeftWidth: 3,
    borderLeftColor: Palette.primary,
  },
  iconBox: { width: 34, height: 34, borderRadius: 10, alignItems: 'center', justifyContent: 'center' },
  itemTopRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 2 },
  itemTitle: { fontSize: 13.5, fontWeight: '700', color: Palette.textTitle },
  unreadDot: { width: 8, height: 8, borderRadius: 4, backgroundColor: Palette.primary },
  itemMessage: { fontSize: 12, color: Palette.textSecondary, lineHeight: 16, marginBottom: 4 },
  itemTime: { fontSize: 10.5, color: Palette.textMuted },
  emptyBox: { paddingVertical: 32, alignItems: 'center', gap: 8 },
  emptyText: { fontSize: 13, color: Palette.textMuted },
  closeBtn: {
    backgroundColor: Palette.backgroundSecondary,
    borderRadius: Radii.button,
    paddingVertical: 12,
    alignItems: 'center',
    marginTop: 12,
    borderWidth: 1,
    borderColor: Palette.border,
  },
  closeBtnText: { fontSize: 13.5, fontWeight: '700', color: Palette.textTitle },
});
